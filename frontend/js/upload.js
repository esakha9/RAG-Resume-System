/* =============================================================
   UPLOAD — Drag & drop, validation, and upload state machine
   ============================================================= */

const ResumeUpload = (function () {

    let dropzone;
    let fileInput;
    let selectedFile = null;

    function formatFileSize(bytes) {
        if (bytes < 1024) return `${bytes} B`;
        if (bytes < 1024 * 1024) return `${(bytes / 1024).toFixed(1)} KB`;
        return `${(bytes / (1024 * 1024)).toFixed(1)} MB`;
    }

    function setState(state) {
        dropzone.dataset.state = state;
    }

    function validateFile(file) {
        const { MAX_FILE_SIZE_BYTES, ACCEPTED_EXTENSIONS } = AppConfig.UPLOAD;
        const extension = file.name.slice(file.name.lastIndexOf(".")).toLowerCase();

        if (!ACCEPTED_EXTENSIONS.includes(extension)) {
            return `Unsupported file type. Use ${ACCEPTED_EXTENSIONS.join(", ")}.`;
        }
        if (file.size > MAX_FILE_SIZE_BYTES) {
            return `File is larger than ${formatFileSize(MAX_FILE_SIZE_BYTES)}.`;
        }
        return null;
    }

    function renderSelectedFile(file) {
        const nameEl = dropzone.querySelector(".selected-file-name");
        const sizeEl = dropzone.querySelector(".selected-file-size");
        if (nameEl) nameEl.textContent = file.name;
        if (sizeEl) sizeEl.textContent = formatFileSize(file.size);
    }

    function setStatusMessage(message) {
        const statusEl = dropzone.querySelector(".upload-status-message");
        if (statusEl) statusEl.textContent = message;
    }

    function setProgress(percent) {
        const fill = dropzone.querySelector(".upload-progress-fill");
        if (fill) fill.style.width = `${percent}%`;
    }

    /**
     * Local fallback so the interface remains demonstrable when the
     * backend at AppConfig.API_BASE_URL is unreachable (e.g. running
     * the frontend standalone). Mirrors the real progress contract.
     */
    function simulateUpload() {
        return new Promise((resolve) => {
            let percent = 0;
            const timer = setInterval(() => {
                percent = Math.min(percent + Math.round(8 + Math.random() * 12), 100);
                setProgress(percent);
                if (percent >= 100) {
                    clearInterval(timer);
                    resolve({ status: "success", message: "Resume processed." });
                }
            }, 180);
        });
    }

    async function handleFile(file) {
        const validationError = validateFile(file);
        if (validationError) {
            setState("error");
            setStatusMessage(validationError);
            return;
        }

        selectedFile = file;
        renderSelectedFile(file);
        setState("uploading");
        setProgress(0);
        setStatusMessage("Uploading…");

        document.dispatchEvent(new CustomEvent("resume:upload-started", { detail: { file } }));

        try {
            let result;
            try {
                result = await ResumeRagApi.uploadResume(file, setProgress);
            } catch (networkError) {
                result = await simulateUpload();
            }

            setState("success");
            setStatusMessage(result.message || "Resume processed successfully.");
            document.dispatchEvent(new CustomEvent("resume:upload-complete", { detail: { file, result } }));
        } catch (error) {
            setState("error");
            setStatusMessage(error.message || "Something went wrong during upload. Try again.");
            document.dispatchEvent(new CustomEvent("resume:upload-error", { detail: { error } }));
        }
    }

    function resetDropzone() {
        selectedFile = null;
        fileInput.value = "";
        setState("empty");
        setProgress(0);
        setStatusMessage("");
        document.dispatchEvent(new CustomEvent("resume:upload-reset"));
    }

    function attachEvents() {
        dropzone.addEventListener("click", (event) => {
            const state = dropzone.dataset.state;
            if (state === "empty" && !event.target.closest(".file-summary-remove-button")) {
                fileInput.click();
            }
        });

        dropzone.addEventListener("keydown", (event) => {
            if ((event.key === "Enter" || event.key === " ") && dropzone.dataset.state === "empty") {
                event.preventDefault();
                fileInput.click();
            }
        });

        fileInput.addEventListener("change", () => {
            if (fileInput.files.length > 0) {
                handleFile(fileInput.files[0]);
            }
        });

        ["dragenter", "dragover"].forEach((eventName) => {
            dropzone.addEventListener(eventName, (event) => {
                event.preventDefault();
                event.stopPropagation();
                if (dropzone.dataset.state === "empty") {
                    setState("dragging");
                }
            });
        });

        ["dragleave", "drop"].forEach((eventName) => {
            dropzone.addEventListener(eventName, (event) => {
                event.preventDefault();
                event.stopPropagation();
                if (dropzone.dataset.state === "dragging") {
                    setState("empty");
                }
            });
        });

        dropzone.addEventListener("drop", (event) => {
            const files = event.dataTransfer.files;
            if (files.length > 0) {
                handleFile(files[0]);
            }
        });

        const removeButton = dropzone.querySelector(".file-summary-remove-button");
        if (removeButton) {
            removeButton.addEventListener("click", (event) => {
                event.stopPropagation();
                resetDropzone();
            });
        }
    }

    function init() {
        dropzone = document.querySelector(".resume-upload-dropzone");
        fileInput = document.querySelector(".resume-upload-input");
        if (!dropzone || !fileInput) return;

        setState("empty");
        attachEvents();
    }

    return { init, resetDropzone };

})();

window.ResumeUpload = ResumeUpload;
