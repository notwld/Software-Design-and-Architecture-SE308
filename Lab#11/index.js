const express = require('express');
const app = express();
const students = require("./students");

console.log(students)

app.use(express.json())

app.get("/",(req,res)=>{
    res.json({msg:"Hello world"})
})

app.get('/get/:id',(req,res)=>{
    const student = students.filter((i,e)=>{
        return i.id==req.params.id
    })
    res.send(student)
})
app.get('/post',(req,res)=>{
    const data = req.body
    console.log(data)
})

app.listen(3000,()=>{
    console.log(`Server running on localhost:3000/`)
})