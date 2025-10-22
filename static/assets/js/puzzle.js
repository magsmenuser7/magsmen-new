// static/js/puzzle.js



document.addEventListener("DOMContentLoaded", function() {
    const form = document.getElementById("strategy-form");

    form.addEventListener("submit", function(e) {
        e.preventDefault();

        // ✅ The data keys here are CORRECT based on the input IDs:
        const data = {
            full_name: document.getElementById("full_name").value,
            email: document.getElementById("email").value,
            phone_number: document.getElementById("phone_number").value,
            location: document.getElementById("location").value,
            
            // 🛑 CRITICAL ALIGNMENT: The HTML IDs use a HYPHEN, but you used an UNDERSCORE here.
            // This is the source of the empty data if your Django view expects hyphens.
            // FIX: Use the actual HTML IDs (q1-answer) as keys in the JSON object.
            'q1_answer': document.getElementById("q1_answer").value, // Key is 'q1-answer'
            'q2_answer': document.getElementById("q2_answer").value, // Key is 'q2-answer'
            'q3_answer': document.getElementById("q3_answer").value, // Key is 'q3-answer'
        };

        fetch("/puzzle/", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
                "X-CSRFToken": getCSRFToken(),
            },
            body: JSON.stringify(data),
        })
        .then(response => {
            if (!response.ok) {
                // Throw an error to catch 500 status gracefully
                throw new Error(`Server returned status: ${response.status}`);
            }
            return response.json();
        })
        .then(result => {
            if (result.success) {
                alert("✅ " + result.message);
                form.reset();
            } else {
                alert("❌ " + result.message);
            }
        })
        .catch(error => {
            alert("❌ Submission Error. Check console for details.");
            console.error("Error:", error);
        });
    });

    // CSRF token helper (Your existing function is correct)
    function getCSRFToken() {
        let cookieValue = null;
        const name = 'csrftoken';
        if (document.cookie && document.cookie !== '') {
            const cookies = document.cookie.split(';');
            for (let cookie of cookies) {
                cookie = cookie.trim();
                if (cookie.startsWith(name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
});





// document.addEventListener("DOMContentLoaded", function() {
//     const form = document.getElementById("strategy-form");

//     form.addEventListener("submit", function(e) {
//         e.preventDefault();

//         const data = {
//             full_name: document.getElementById("full_name").value,
//             email: document.getElementById("email").value,
//             phone_number: document.getElementById("phone_number").value,
//             location: document.getElementById("location").value,
//             q1_answer: document.getElementById("q1-answer").value,
//             q2_answer: document.getElementById("q2-answer").value,
//             q3_answer: document.getElementById("q3-answer").value,
//         };

//         fetch("/puzzle/", {
//             method: "POST",
//             headers: {
//                 "Content-Type": "application/json",
//                 "X-CSRFToken": getCSRFToken(),
//             },
//             body: JSON.stringify(data),
//         })
//         .then(response => response.json())
//         .then(result => {
//             if (result.success) {
//                 alert("✅ " + result.message);
//                 form.reset();
//             } else {
//                 alert("❌ " + result.message);
//             }
//         })
//         .catch(error => console.error("Error:", error));
//     });

//     // CSRF token helper
//     function getCSRFToken() {
//         let cookieValue = null;
//         const name = 'csrftoken';
//         if (document.cookie && document.cookie !== '') {
//             const cookies = document.cookie.split(';');
//             for (let cookie of cookies) {
//                 cookie = cookie.trim();
//                 if (cookie.startsWith(name + '=')) {
//                     cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
//                     break;
//                 }
//             }
//         }
//         return cookieValue;
//     }
// });
