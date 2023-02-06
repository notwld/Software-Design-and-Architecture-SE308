const express = require('express');
const students = require('./student'); 
const app=express();
const port=8080;

app.use(express.json());
app.get('/',(req, res)=>{
    res.json(students);

});

app.post('/students', (req, res)=>{

    const user = {
        id: students.length+1, 
        first_name : req.body.first_name, 
        last_name: req.body.last_name,
        email: req.body.email
    } 
    students.push(user);
    res.json(user)
});
app.listen(port,()=>{
    console.log('server start',port);
});