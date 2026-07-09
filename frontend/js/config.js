/* =============================================================
   CONFIG — Application-wide constants and API configuration
   ============================================================= */

const AppConfig = Object.freeze({

    // Base URL of the RAG backend. Override by defining
    // `window.__RESUME_RAG_API_BASE__` before this script loads
    // (e.g. injected by a deployment pipeline).
    API_BASE_URL: window.__RESUME_RAG_API_BASE__ || "http://localhost:8000",

    ENDPOINTS: {
        UPLOAD: "/upload",
        ASK: "/ask"
    },

    UPLOAD: {
        MAX_FILE_SIZE_BYTES: 10 * 1024 * 1024, // 10MB
        ACCEPTED_TYPES: [
            "application/pdf",
            "application/msword",
            "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
        ],
        ACCEPTED_EXTENSIONS: [".pdf", ".doc", ".docx"]
    },

    CHAT: {
        MAX_QUESTION_LENGTH: 800
    },

    STORAGE_KEYS: {
        THEME: "resumeRag.theme",
        SIDEBAR_COLLAPSED: "resumeRag.sidebarCollapsed"
    }

});

// Exposed for other modules loaded as plain scripts (no bundler in use).
window.AppConfig = AppConfig;
