/* =============================================================
   MAIN — Application bootstrap: theme, sidebar, wiring modules
   ============================================================= */

(function () {

    /* ---------- Theme ---------- */

    function initTheme() {
        const toggle = document.querySelector(".theme-toggle-button");
        const stored = localStorage.getItem(AppConfig.STORAGE_KEYS.THEME);
        const prefersDark = window.matchMedia("(prefers-color-scheme: dark)").matches;
        const theme = stored || (prefersDark ? "dark" : "light");

        applyTheme(theme);

        if (toggle) {
            toggle.addEventListener("click", () => {
                const next = document.documentElement.dataset.theme === "dark" ? "light" : "dark";
                applyTheme(next);
                localStorage.setItem(AppConfig.STORAGE_KEYS.THEME, next);
            });
        }
    }

    function applyTheme(theme) {
        if (theme === "dark") {
            document.documentElement.setAttribute("data-theme", "dark");
        } else {
            document.documentElement.removeAttribute("data-theme");
        }
    }

    /* ---------- Sidebar ---------- */

    function initSidebar() {
        const sidebar = document.querySelector(".application-sidebar");
        const collapseButton = document.querySelector(".sidebar-collapse-button");
        if (!sidebar) return;

        const stored = localStorage.getItem(AppConfig.STORAGE_KEYS.SIDEBAR_COLLAPSED) === "true";
        sidebar.dataset.collapsed = String(stored);

        if (collapseButton) {
            collapseButton.addEventListener("click", () => {
                const collapsed = sidebar.dataset.collapsed !== "true";
                sidebar.dataset.collapsed = String(collapsed);
                localStorage.setItem(AppConfig.STORAGE_KEYS.SIDEBAR_COLLAPSED, String(collapsed));
            });
        }

        highlightActiveNavItem(sidebar);
    }

    function highlightActiveNavItem(sidebar) {
        const currentPage = document.body.dataset.page;
        sidebar.querySelectorAll(".navigation-menu-item").forEach((item) => {
            if (item.dataset.page === currentPage) {
                item.setAttribute("aria-current", "page");
            } else {
                item.removeAttribute("aria-current");
            }
        });
    }

    /* ---------- Processing status, driven by upload lifecycle events ---------- */

    function initProcessingStatus() {
        const steps = document.querySelectorAll(".processing-step");
        const overallFill = document.querySelector(".processing-overall-bar-fill");
        const overallLabel = document.querySelector(".processing-overall-label .text-mono, .processing-overall-percent");

        const sequence = ["resume", "embedding", "vector", "llm"];

        function setStep(name, state) {
            const step = document.querySelector(`.processing-step[data-step="${name}"]`);
            if (step) step.dataset.state = state;
        }

        function setOverall(percent) {
            if (overallFill) overallFill.style.width = `${percent}%`;
            const percentLabel = document.querySelector(".processing-overall-percent");
            if (percentLabel) percentLabel.textContent = `${percent}%`;
        }

        document.addEventListener("resume:upload-started", () => {
            sequence.forEach((name) => setStep(name, "pending"));
            setStep("resume", "active");
            setOverall(10);
        });

        document.addEventListener("resume:upload-complete", () => {
            let delay = 0;
            const stepDelay = 500;
            setStep("resume", "complete");
            setOverall(25);

            sequence.slice(1).forEach((name, index) => {
                delay += stepDelay;
                setTimeout(() => {
                    setStep(name, "active");
                    setOverall(25 + (index + 1) * 25 - 15);
                }, delay);
                setTimeout(() => {
                    setStep(name, "complete");
                    setOverall(25 + (index + 1) * 25);
                }, delay + stepDelay);
            });

            setTimeout(() => {
                setOverall(100);
                if (window.ResumeChat) {
                    ResumeChat.setResumeReady(true);
                }
            }, delay + stepDelay + 100);
        });

        document.addEventListener("resume:upload-error", () => {
            setStep("resume", "error");
        });

        document.addEventListener("resume:upload-reset", () => {
            sequence.forEach((name) => setStep(name, "pending"));
            setOverall(0);
            if (window.ResumeChat) {
                ResumeChat.setResumeReady(false);
            }
        });
    }

    /* ---------- Mobile sidebar toggle (hooked to a header control if present) ---------- */

    function initMobileSidebarToggle() {
        const sidebar = document.querySelector(".application-sidebar");
        const toggle = document.querySelector("[data-mobile-nav-toggle]");
        if (!sidebar || !toggle) return;

        toggle.addEventListener("click", () => {
            const isOpen = sidebar.dataset.mobileOpen === "true";
            sidebar.dataset.mobileOpen = String(!isOpen);
        });

        document.addEventListener("click", (event) => {
            const isOpen = sidebar.dataset.mobileOpen === "true";
            if (!isOpen) return;
            if (sidebar.contains(event.target) || toggle.contains(event.target)) return;
            sidebar.dataset.mobileOpen = "false";
        });

        sidebar.querySelectorAll(".navigation-menu-item").forEach((item) => {
            item.addEventListener("click", () => {
                sidebar.dataset.mobileOpen = "false";
            });
        });
    }

    /* ---------- Settings page toggles (only present on pages/settings.html) ---------- */

    function initSettingsPage() {
        const darkModeToggle = document.getElementById("settings-dark-mode-toggle");
        const sidebarToggle = document.getElementById("settings-sidebar-toggle");
        if (!darkModeToggle && !sidebarToggle) return;

        if (darkModeToggle) {
            darkModeToggle.checked = document.documentElement.dataset.theme === "dark";
            darkModeToggle.addEventListener("change", () => {
                const next = darkModeToggle.checked ? "dark" : "light";
                applyTheme(next);
                localStorage.setItem(AppConfig.STORAGE_KEYS.THEME, next);
            });
        }

        if (sidebarToggle) {
            const sidebar = document.querySelector(".application-sidebar");
            sidebarToggle.checked = localStorage.getItem(AppConfig.STORAGE_KEYS.SIDEBAR_COLLAPSED) === "true";
            sidebarToggle.addEventListener("change", () => {
                localStorage.setItem(AppConfig.STORAGE_KEYS.SIDEBAR_COLLAPSED, String(sidebarToggle.checked));
                if (sidebar) sidebar.dataset.collapsed = String(sidebarToggle.checked);
            });
        }
    }

    /* ---------- Bootstrap ---------- */

    function init() {
        initTheme();
        initSidebar();
        initMobileSidebarToggle();
        initProcessingStatus();
        initSettingsPage();

        if (window.ResumeUpload) ResumeUpload.init();
        if (window.ResumeChat) ResumeChat.init();
    }

    if (document.readyState === "loading") {
        document.addEventListener("DOMContentLoaded", init);
    } else {
        init();
    }

})();
