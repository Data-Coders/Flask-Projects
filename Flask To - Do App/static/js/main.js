document.querySelectorAll('.danger').forEach(item => {
	item.addEventListener("mouseenter", event => {
		document.body.style.backgroundColor = "red";
		document.getElementById('namee').innerHTML = "<b>Danger</b>";
	})
})

document.querySelectorAll('.danger2').forEach(item => {
	item.addEventListener("mouseenter", event => {
		document.body.style.backgroundColor = "red";
		document.getElementById('namee').innerHTML = "<b>Danger</b>";
	})
})



function ready() {
	document.body.style.backgroundColor = `purple`;
	console.log("This is in Development. \nDo consider to find my Website");
	console.log("Please Head on to My webSite : https://amanojha.xyz")
}

document.addEventListener("DOMContentLoaded", ready);

document.querySelectorAll('.danger').forEach(item => {
	item.addEventListener("mouseleave", event => {
		document.body.style.backgroundColor = `purple`;
		document.getElementById('namee').innerHTML = "<b> </b>";
	})
})

document.querySelectorAll('edit').forEach(item => {
	item.addEventListener("mouseenter", event => {
		document.body.style.backgroundColor = "rgb(255, 8, 100)";
	})
})

document.querySelectorAll('edit2').forEach(item => {
	item.addEventListener("mouseenter", event => {
		document.body.style.backgroundColor = "rgb(255, 8, 100)";
	})
})

document.querySelectorAll('.edit').forEach(item => {
	item.addEventListener("mouseenter", event => {
		document.body.style.backgroundColor = "rgb(255, 8, 100)";
	})
})

document.querySelectorAll('.edit').forEach(item => {
	item.addEventListener("mouseleave", event => {
		document.body.style.backgroundColor = `purple`;
		document.getElementById('namee').innerHTML = "<b> </b>";
	})
})

document.querySelectorAll('.edit2').forEach(item => {
	item.addEventListener("mouseleave", event => {
		document.body.style.backgroundColor = "rgb(255, 8, 100)";
		document.getElementById('namee').innerHTML = "<b> </b>";
	})
})