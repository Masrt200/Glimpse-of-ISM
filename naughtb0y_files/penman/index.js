const express = require("express")
const jwt = require("jsonwebtoken")
const cookieParser = require("cookie-parser")
const bodyparser = require("body-parser")
const path = require("path")


const app = express()
app.set('view engine', 'ejs');
app.use(cookieParser())
app.use(bodyparser.urlencoded({ extended: false }))

const jwt_secret=process.env.JWT_SECRET||"ihatethispart"

const flag="fest ke inaguration mie mat chale jana kabhi, bahut bore hoge \n iog{dance_dekhne_jao_director_ko_nhi!} \n DIAMOND: the_heart_of_ism"

function str_rot13(str) {
    return (str + '').replace(/[a-zA-Z]/gi, function (s) {
        return String.fromCharCode(s.charCodeAt(0) + (s.toLowerCase() < 'n' ? 13 : -13))
    })
}

function signJWT(data) {
    return jwt.sign(data, jwt_secret,{noTimestamp:true});
}

app.get("/", (req, res) => {
    res.render('login')
})

app.get("/flag", async(req, res) => {
    var cookie = req.cookies;
    
    try{
        await jwt.verify(cookie['token'], jwt_secret, (err, authData) => {
            if (err) {
                res.status(403).render('403')
            }
            else {
                var decoded = jwt.decode(cookie['token'])
                if (decoded.faccha === str_rot13('true')) {
                    res.status(403).render('403')
                    return;
                }
                else {
                    res.render('flag')
                }
            }
        })

    
}    catch (err) {
        console.log(err)
    }
})

app.post("/login", (req, res) => {
    var username = req.body.username
  	var password = req.body.password
    if (username && password) { 
        var token = signJWT({ "user": str_rot13(username), "faccha": str_rot13("true") })
        res.cookie('token', token, { maxAge: 900000, httpOnly: true });
        res.render('dashboard')
    }
    else {
        res.send("What are you trying to do")
    }
})

const port = process.env.PORT || 5555
app.listen(port, () => { console.log(`server started on ${port}`) })