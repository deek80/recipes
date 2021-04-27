import React from "react";
import {makeStyles} from "@material-ui/core";

const useStyles = makeStyles({
  root: {
    height: "100vh",
    width: "100vw",
    backgroundColor: "orange",
  },
});

const App = () => {
  const classes = useStyles();
  return <div className={classes.root}>TEST 1 2</div>;
};

export default App;
