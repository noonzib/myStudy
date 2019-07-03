function addOnclick(){
    var len = document.getElementsByTagName("span").length;
    var i;
    for(i=0;i<len;i++){
        document.getElementsByTagName("span")[i].setAttribute("onclick","link(this.id)");
    }
}
window.onload = addOnclick;
