/* =============================================================
   API — Backend communication layer
   Talks to the existing RAG backend:
     POST /upload  -> multipart/form-data resume file
     POST /ask     -> { question } JSON, returns answer + context
   ============================================================= */

const ResumeRagApi = (function () {

    function buildUrl(endpoint) {
        return `${AppConfig.API_BASE_URL}${endpoint}`;
    }

    /**
     * Uploads a resume file with progress reporting.
     * Uses XMLHttpRequest because fetch() cannot report upload progress.
     *
     * @param {File} file
     * @param {(percent: number) => void} onProgress
     * @returns {Promise<{status: string, message: string}>}
     */
    function uploadResume(file, onProgress) {
        return new Promise((resolve, reject) => {
            const formData = new FormData();
            formData.append("resume", file, file.name);

            const request = new XMLHttpRequest();
            request.open("POST", buildUrl(AppConfig.ENDPOINTS.UPLOAD), true);

            request.upload.addEventListener("progress", (event) => {
                if (event.lengthComputable && typeof onProgress === "function") {
                    const percent = Math.round((event.loaded / event.total) * 100);
                    onProgress(percent);
                }
            });

            request.addEventListener("load", () => {
                if (request.status >= 200 && request.status < 300) {
                    try {
                        const data = request.responseText ? JSON.parse(request.responseText) : {};
                        resolve(data);
                    } catch (parseError) {
                        resolve({ status: "success", message: "Resume uploaded." });
                    }
                } else {
                    reject(new Error(`Upload failed with status ${request.status}`));
                }
            });

            request.addEventListener("error", () => {
                reject(new Error("Could not reach the resume processing service."));
            });

            request.send(formData);
        });
    }

    /**
     * Sends a question to the RAG backend and returns the answer
     * along with the retrieved supporting chunks.
     *
     * @param {string} question
     * @returns {Promise<{answer: string, context: Array<{chunk: string, score: number}>}>}
     */
    async function askQuestion(question) {
        const response = await fetch(buildUrl(AppConfig.ENDPOINTS.ASK), {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ question })
        });

        if (!response.ok) {
            throw new Error(`Request failed with status ${response.status}`);
        }

        return response.json();
    }

    return {
        uploadResume,
        askQuestion
    };

})();

window.ResumeRagApi = ResumeRagApi;
