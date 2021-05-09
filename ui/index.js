const JoinBtn = document.querySelector(".join");
const SettingsBtn = document.querySelector(".settings");
const AboutBtn = document.querySelector(".about");

const ChatScreen = document.querySelector(".chat");
const IntroScreen = document.querySelector(".intro");

const UserNameInp = document.querySelector("#username");
const ServerNameInp = document.querySelector("#servername");

const ServerNameLbl = document.querySelector(".decor-text");
const MembersLst = document.querySelector(".list");
const Messages = document.querySelectorAll(".msg");
const MsgsContainer = document.querySelector(".msgs ul");

const NewMsgBody = document.querySelector(".msg-to-send");

let metadata;

JoinBtn.addEventListener('click', async _ => {
	let username = UserNameInp.value;
	let servername = ServerNameInp.value;
	
	// Presence Check
	if (username && servername) {
		if (isValid(servername)) {
			pywebview.api.initializeServer(servername, username).then(_ => {
				IntroScreen.style.display = "none";
				ChatScreen.style.display = "block";

				// Set Timers
				// Check MetaData
				setInterval(async () => {
					// If the metadata was changed, show updated version.
					pywebview.api.getMetadata().then(md => {
						if (md.server_name != metadata.server_name && arraysEqual(md.members, metadata.members)) {
							metadata = md;
							ServerNameLbl.innerText = metadata.server_name;
							for (let i = 0; i < MembersLst.length; i++) {
								/*
								<li class="member">
							      <div class="about">
							        <div class="name">Em Dash -&nbsp;<b class="typing">typing</b></div>
							        <div class="status"><i class="online">Online</i></div>
							      </div>
							    </li>
								*/
								let member = document.createElement("li");
								member.className = "member";
								let about = document.createElement("div");
								about.className = "about";
								let name = document.createElement("div");
								name.className = "name";
								name.innerText = metadata.members[i];
								let status = document.createElement("div");
								status.className = "status";
								let online = document.createElement("i");
								online.className = "online";
								online.innerText = "Online";
								status.appendChild(online);
								about.appendChild(name);
								about.appendChild(status);
								member.appendChild(about);
							}
						}
					});	
				}, 250);

				// Check Messages
				setInterval(async () => {
					pywebview.api.getMessages().then(msgs => {
						if (msgs.length != Messages.length) {
							for (var i = Messages.length + 1; i < msgs.length; i++) {
								let author = msgs[i].author;
								let content = msgs[i].content;
								// <div class="msg"><b class="author">Em Dash:&nbsp;</b>Hello</div>
								let msg = document.createElement("li");
								let div = document.createElement("div");
								div.className = "msg";
								let name = document.createElement("b");
								name.className = "author";
								name.innerText = `${author}:&nbsp;`;
								div.appendChild(name);
								div.appendChild(document.createTextNode(content));
								msg.appendChild(div);

								MsgsContainer.appendChild(msg);
							}
						}
					});
				}, 250);

				NewMsgBody.addEventListener('keypress', async _ => {
					let key = window.event.keyCode;

					// If the user has pressed enter
					if (key === 13 && NewMsgBody.value) {
						pywebview.api.sendMessage({
							'content': NewMsgBody.value,
							'author': username
						}).then(() => {});
					}
				});
			});
    	}
	}
});

const isUnique = async username => {
	return pywebview.api.getMetadata().then(metadata => {
		return metadata.members.contains(username);
	});
};

const isValid = async servername => {
	return pywebview.api.isValidUri(servername).then(bool => {
		return bool;
	});
};

function arraysEqual(a, b) {
  if (a === b) return true;
  if (a == null || b == null) return false;
  if (a.length !== b.length) return false;

  for (var i = 0; i < a.length; ++i) {
    if (a[i] !== b[i]) return false;
  }
  return true;
}