import express from "express"
import mysql from "mysql2"
import cors from "cors"

const app = express()

const db = mysql.createConnection({
    host:"localhost",
    user:"root",
    password:"S@nktum56",
    database:"new"
})

app.use(cors())

// app.get("/", (req, res) => {
//     res.json("hello this is the backend!")
// })

app.get("/", (req, res) => {
    const q = "SELECT * FROM new.peoples;";
    db.query(q, (err, data) => {
        if (err) return res.json(err);
        res.json(data);
    })
})
app.listen(5000, () => {
    console.log("Connected to backend!");
})