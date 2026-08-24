const fileInput = document.getElementById("fileInput");
const analyzeButton = document.getElementById("analyzeButton");
const statusText = document.getElementById("status");

const resultsSection = document.getElementById("results");

const extractedText = document.getElementById("extractedText");
const sentiment = document.getElementById("sentiment");
const engagementScore = document.getElementById("engagementScore");
const wordCount = document.getElementById("wordCount");
const readability = document.getElementById("readability");

const keywords = document.getElementById("keywords");
const hashtags = document.getElementById("hashtags");
const cta = document.getElementById("cta");
const suggestions = document.getElementById("suggestions");


analyzeButton.addEventListener("click", async () => {

    const file = fileInput.files[0];

    // Check whether a file was selected
    if (!file) {
        statusText.textContent = "Please select a PDF or image first.";
        return;
    }


    // Show loading message
    statusText.textContent = "Analyzing your content...";
    analyzeButton.disabled = true;


    // Create form data
    const formData = new FormData();

    formData.append("file", file);


    try {

        // Send file to FastAPI
        const response = await fetch(
            "http://127.0.0.1:8000/analyze-file",
            {
                method: "POST",
                body: formData
            }
        );


        const data = await response.json();


        // Handle backend errors
        if (!response.ok) {
            throw new Error(
                data.detail || "Something went wrong."
            );
        }


        // -------------------------
        // Display extracted text
        // -------------------------

        extractedText.textContent = data.extracted_text;


        const analysis = data.analysis;


        // -------------------------
        // Display metrics
        // -------------------------

        sentiment.textContent =
            analysis.sentiment;


        engagementScore.textContent =
            `${analysis.engagement_score}/100`;


        wordCount.textContent =
            analysis.word_count;


        if (analysis.readability_score !== null) {
            readability.textContent =
                analysis.readability_score;
        } else {
            readability.textContent = "N/A";
        }


        // -------------------------
        // Display keywords
        // -------------------------

        keywords.innerHTML = "";

        analysis.keywords.forEach(keyword => {

            const tag = document.createElement("span");

            tag.className = "tag";

            tag.textContent = keyword;

            keywords.appendChild(tag);
        });


        // -------------------------
        // Display hashtags
        // -------------------------

        hashtags.innerHTML = "";

        if (analysis.hashtags.length === 0) {

            hashtags.textContent =
                "No hashtags found.";

        } else {

            analysis.hashtags.forEach(hashtag => {

                const tag = document.createElement("span");

                tag.className = "tag";

                tag.textContent = hashtag;

                hashtags.appendChild(tag);
            });
        }


        // -------------------------
        // Display CTA
        // -------------------------

        if (analysis.call_to_action.present) {

            cta.textContent =
                "CTA detected: " +
                analysis.call_to_action.detected.join(", ");

        } else {

            cta.textContent =
                "No clear call-to-action detected.";
        }


        // -------------------------
        // Display suggestions
        // -------------------------

        suggestions.innerHTML = "";

        analysis.suggestions.forEach(suggestion => {

            const item = document.createElement("li");

            item.textContent = suggestion;

            suggestions.appendChild(item);
        });


        // Show results
        resultsSection.classList.remove("hidden");

        statusText.textContent =
            "Analysis completed successfully!";


    } catch (error) {

        console.error(error);

        statusText.textContent =
            "Error: " + error.message;

    } finally {

        analyzeButton.disabled = false;
    }

});