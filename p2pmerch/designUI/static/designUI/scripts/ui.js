var circle;
var clicked = true;

const onMouseMove = (e) =>{
    circle.style.left = e.pageX + 'px';
    circle.style.top = e.pageY + 'px';
}

const onMouseClick = (e) => {
    if (clicked) {
        clicked = false;
        document.addEventListener("mousemove", onMouseMove)
    } else {
        clicked = true;
        document.removeEventListener("mousemove", onMouseMove)
    }
}

window.addEventListener('load', function () {
    circle = document.getElementById('image-box');
    document.addEventListener('mousemove', onMouseMove);
    this.document.addEventListener('click', onMouseClick)
})
