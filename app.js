const express = require('express');
const bodyParser = require('body-parser');
const app = express();
const port = 80;
const { exec } = require('child_process');


app.use(express.static(`${__dirname}/public`));
app.set('view engine', 'pug');
app.set('views', `${__dirname}/views`);

app.use(bodyParser.urlencoded({ extended: true, limit: '30mb' }));
app.use(bodyParser.json({ extended: true, limit: '30mb' }));



app.get("/", (req, res, next) => {
    res.render('main/index');
})

app.post("/", (req, res, next) => {
    var { symbols } = req.body;
    console.log(symbols);
    exec(`python ./portfolio_api.py ${symbols}`, (eror, stdout, stderr) => {
        // stdout = JSON.parse(stdout);
        res.render("main/index", { stdout });
    })
    // res.redirect("/");
})
// test


app.get('*', (req, res, next) => {
    res.status(404).render('404/index');
    // res.render('comingsoon/index');
});
app.get('*', (err, req, res, next) => {
    res.status(500).render('500/index');
});


app.listen(port, () => {
    console.warn(`server running at port ${port}`);
});