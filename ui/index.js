const JoinBtn = document.querySelector(".join");
const SettingsBtn = document.querySelector(".settings");
const AboutBtn = document.querySelector(".about");

const ChatScreen = document.querySelector(".chat");
const IntroScreen = document.querySelector(".intro");

JoinBtn.addEventListener('click', _ => {
    IntroScreen.style.display = "none";
    ChatScreen.style.display = "block";
});