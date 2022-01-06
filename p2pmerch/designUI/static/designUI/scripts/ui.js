var userImg;
var clicked = true;

const onMouseMove = (e) =>{
    userImg.style.left = e.pageX + 'px';
    userImg.style.top = e.pageY + 'px';
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

function saveWork() {
    design = document.getElementById("image")
    boundingBox = document.getElementById("design-bounds")
    boundingBoxOffsets = boundingBox.getBoundingClientRect();
    offsets = design.getBoundingClientRect();
    console.log(design)
    console.log(offsets.top-boundingBoxOffsets.top)
    console.log(offsets.left-boundingBoxOffsets.left)
    console.log(offsets.width)
    console.log(offsets.height)
}

window.addEventListener('load', function () {
    userImg = document.getElementById('image-box');
    document.addEventListener('mousemove', onMouseMove);
    userImg.addEventListener('click', onMouseClick);
})
