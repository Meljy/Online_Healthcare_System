// JavaScript loaded and ready
console.log("JAVASCRIPT Here!");


document.addEventListener("DOMContentLoaded", () => {
    console.log("DOM fully loaded and parsed.");

    //dynamic greeting
    const contentBlock = document.querySelector("body");
    const greetingDiv = document.createElement("div");
    greetingDiv.id = "dynamicGreeting";
    greetingDiv.style.margin = "20px";
    greetingDiv.style.textAlign = "center";
    greetingDiv.style.color = "blue";
    greetingDiv.innerText = "Welcome to Healthcare System!";
    contentBlock.prepend(greetingDiv);

    //interactive button
    const button = document.createElement("button");
    button.id = "clickMeButton";
    button.style.margin = "10px auto";
    button.style.display = "block";
    button.innerText = "Click Me!";
    contentBlock.appendChild(button);

    // click functionality
    button.addEventListener("click", () => {
        console.log("Button clicked!");
        alert("Hello This is you guide to use the System!");
        alert("If you click me means you curios to this!");
        alert("Click (HOME) if you are you finish to your schedule or want to refresh!");
        alert("Click (ABOUT) to see the all information!");
        alert("Click (PATIENT) if you want to schedule and appoinment!");
        alert("Click (Doctors) To See Available Doctors");
        alert("Click (Contact) To see information to Contact Us!");
        alert("Click (Emergency) To Call Ambulance!");
        alert("Click (Logout) if you want Out!");
        // Toggle visibility of greetingDiv
        if (greetingDiv.style.display === "none") {
            greetingDiv.style.display = "block";
        } else {
            greetingDiv.style.display = "none";
        }
    });
});
