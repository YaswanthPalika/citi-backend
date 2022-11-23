const mongoose = require("mongoose");
const express = require("express");

//Food schema
const UserSchema = new mongoose.Schema({
  username: {
    type: String,
    required: true,
  },
  password: {
    type: String,
  },
});

module.exports = new mongoose.model("User", UserSchema);
