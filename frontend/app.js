let claimId = "";

function startClaim() {
  fetch("http://127.0.0.1:8000/claim/start", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({
      policy_number: document.getElementById("policy").value,
      claim_type: document.getElementById("type").value,
      incident_date: "2026-01-06",
      incident_location: document.getElementById("location").value,
      description: document.getElementById("desc").value
    })
  })
  .then(res => res.json())
  .then(data => {
    claimId = data.claim_id;
    document.getElementById("uploadSection").style.display = "block";
    alert("Claim Created: " + claimId);
  });
}

function uploadDoc() {
  let formData = new FormData();
  formData.append("file", document.getElementById("file").files[0]);

  fetch(`http://127.0.0.1:8000/documents/upload/${claimId}`, {
    method: "POST",
    body: formData
  })
  .then(res => res.json())
  .then(data => {
    document.getElementById("result").innerHTML =
      `<b>AI Damage Type:</b> ${data.ai_damage_type}<br>
       <b>Severity:</b> ${data.ai_severity}`;
  });
}
