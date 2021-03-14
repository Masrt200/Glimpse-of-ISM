const express = require("express")
const path = require("path")
// var sleep = require("sleep")
const bodyparser=require("body-parser")

const app = express()

app.use(express.static(path.join(__dirname+"/public")))
app.use(bodyparser.urlencoded({extended:false}))
app.use(express.json())

app.get("/", (req, res) => {
    res.redirect("/Good")
})

app.get("/Good", (req, res) => {
    res.redirect("/Evening")
})

app.get("/Evening", (req, res) => {
    res.redirect("/Respected")
})

app.get("/Respected", (req, res) => {
    res.redirect("/Senior")
})


app.get("/Senior", (req, res) => {
    res.redirect("/my_name")
})
app.get("/my_name", (req, res) => {
    res.redirect("/is")
})
app.get("/is", (req, res) => {
    res.redirect("/NOob.")
})
app.get("/NOob.", (req, res) => {
    res.redirect("/I_am_from_NOobTown,")
})

app.get("/I_am_from_NOobTown,", (req, res) => {
    res.redirect("/India.")
})

app.get("/India.", (req, res) => {
    res.redirect("/I_am_pursuing")
})

app.get("/I_am_pursuing", (req, res) => {
    res.redirect("/BTECH")
})

app.get("/BTECH", (req, res) => {
    res.redirect("/in_Hackergiri.")
})

app.get("/in_Hackergiri.", (req, res) => {
    res.redirect("/My_hobby")
})

app.get("/My_hobby", (req, res) => {
    res.redirect("/is_hawking.")
})
app.get("/is_hawking.", (req, res) => {
    res.redirect("/I_want_a_flag_plzzzz.")
})

app.get("/I_want_a_flag_plzzzz.", (req, res) => {
    res.redirect("/OK_then")
})

app.get("/OK_then", (req, res) => {
    res.redirect("/send_me_a_POST")
})
app.get("/send_me_a_POST", (req, res) => {
    res.redirect("/at_my_hostel.")
})
app.get("/at_my_hostel.", (req, res) => {
    res.redirect("/aur_dhang_se_intro_de")
})
app.get("/aur_dhang_se_intro_de", (req, res) => {
    res.send("SOme html or ejs here\n")
})


app.post("/login1", (req, res) => {
    const { username, password }=req.body
    // console.log(username,password)
    if (username != "admin") {
        res.send("You noob you really thought that?\n enumerate more see the styles\n")
        //todo make an html or ejs file 
    }
    else {
        res.send("its a rabbit hole why you dont get it!!\n")
        //todo make an html or ejs file with rick roll
    }
})

app.post("/amber", (req, res) => {
    let name = req.body.name
    let place = req.body.place
    let branch=req.body.branch
    if (name != undefined&& place != undefined &&branch != undefined ) {
        res.send("postcard toh mil gya, but handwriting is bad. Marks will be the penalty \n iog{pehle_nhi_jaati_thi_dash_dash} \n SAC: where_we_will_meet_the_most")
        //todo make an ejs or html
    }
    else {
        res.send("you fool do you send the letter empty,send a POSTcard with your name,place,branch in json\n")
        //todo make an html or ejs file
    }
})

app.get("/amber", (req, res) => {
    res.send("I clearly told you to send A POSTcard !!!!! \n NOoooooooob!!!")
})

port=process.env.PORT||4444
app.listen(port,()=>console.log(`server started!!!!! at port ${port}`))