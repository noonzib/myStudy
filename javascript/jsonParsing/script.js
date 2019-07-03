var data = '{"toa1": "a1.html","toa2": "a2.html","toa3": "a3.html","toli": "list.html"}';
function link(id){
    obj = JSON.parse(data);
    for(idName in obj){
        if(id == idName){
            location.href = obj[idName];
        }
    }
}   