import React from 'react';
// import logo from './logo.svg';
import NavBar from "./components/NavBar";
import { useAuth0 } from "./react-auth0-spa";
import { Router, Route, Switch } from "react-router-dom";
import Profile from "./components/Profile";
import history from "./utils/history";
import PrivateRoute from "./components/PrivateRoute";
import { RouteMovies } from './components/MovieView';
// import { RouteActors } from './components/Actors';
import './App.css';

function App() {
  const { loading } = useAuth0();

  if (loading) {
    return <div>Loading...</div>;
  }

  return (
    <div className="App">
      <Router history={history}>
        <header>
          <NavBar />
        </header>
        <Switch>
          <Route path="/" exact/>
          <Route path='/movies' component={RouteMovies} />
          {/* <Route path='/actors' component={RouteActors} /> */} 
          {/* <PrivateRoute path="/profile" component={Profile} /> */}
        </Switch>
      </Router>
    </div>
  );
}

export default App;
