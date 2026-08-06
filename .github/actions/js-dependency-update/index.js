const core = require("@actions/core");
const exec = require("@actions/exec");
const github = require("@actions/github");
async function run() {

    // parse inputs
        // base branch
        // target branch
        // github token
        // working directory
    // exec npm update
    // check whether package*.json are modified
    // create PR if there are changes, otherwise - finish the workflow
    core.info("I'm a basic action!");
}

run()