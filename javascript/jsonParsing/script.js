var data = 
{
    "toa1": [
        "a1.html"
    ],
    "toa2": [
        "a2.html"
    ],
    "toa3": [
        "a3.html"
    ],
    "toli": [
        "list.html"
    ]
};
function getIdName(id){
    var thisId=id;
    link(thisId);
}
function link(id){
    var link = JSON.parse(data).thisId;
    location.href = link;
}