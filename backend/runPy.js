const { spawn}=require('child_process');
function searchProduct(searchWord){
const dataRead=[];
    const childPy=spawn('python',['../webscraper.py',...searchWord]);
    // childPy.stdout.on('data',(data)=>{
    //     dataRead=data;
    //     console.log(`${data}`);
    // })

    childPy.stderr.on('data',(data)=>{console.log(data);});
    childPy.on('close',()=>{console.log('Closed');});
return dataRead;}
    module.exports = searchProduct;