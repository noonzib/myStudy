var data = 
{
    "toaList": [
        "a1.html",
        "a2.html",
        "a3.html"
    ],
    "toli":[
        "list.html"
    ]
};
function link(id, index){
    var obj = JSON.stringify(data);
    obj = JSON.parse(obj);
    for(idName in obj){
        if(id == idName){
            location.href = obj[idName][index];
        }
    }
}   