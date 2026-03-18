const express = require('express');
const app = express();

app.get('/accounts', (req, res) => {
    res.json({ message: "Account Service Working" });
});

app.listen(3000, '0.0.0.0', () => {
    console.log("Account service running on port 3000");
});