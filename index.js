const mongoose = require("mongoose");
const express = require("express");
const cors = require("cors");
const app = express();
const User = require("./models/index");
const { spawn } = require("child_process");
//middleware
app.use(express.json());
app.use(express.urlencoded({ extended: false }));
app.use(cors());

//mongo db connection
const url = `mongodb+srv://yas:yas@cluster0.wdszhtf.mongodb.net/?retryWrites=true&w=majority`;

const connectionParams = {
  useNewUrlParser: true,

  useUnifiedTopology: true,
};
mongoose
  .connect(url, connectionParams)
  .then(() => {
    console.log("Connected to database ");
  })
  .catch((err) => {
    console.error(`Error connecting to the database. \n${err}`);
  });

//server running
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
  console.log("server started at PORT ", PORT);
});

//post request to mongoose
app.post("/", (req, res) => {
  const { username, password } = req.body;
  console.log(username, password);
  user = new User({
    username: username,
    password: password,
  });
  user
    .save()
    .then(() => res.send("uploaded successfully"))
    .catch((e) => res.send("failed").status(500));
});

app.post("/main", async (req, res) => {
  const { data } = req.body;
  //console.log(typeof data, data);
  const jdata = JSON.stringify(data);
  const x = jdata;
  console.log("yes");
  const process = await spawn("python3", ["./test2.py", x]);
  process.stdout.on("data", function (data) {
    console.log(data.toString());
    res.send(data.toString());
  });
});
