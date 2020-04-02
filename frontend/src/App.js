import React from 'react';
// import logo from './logo.svg';
import { NavBar } from "./components/NavBar";
import { useAuth0 } from "./react-auth0-spa";
import { Router, Route, Switch } from "react-router-dom";
import history from "./utils/history";
import { RouteMovies } from './components/MovieView';
import { Home } from './components/Home';
import { Container } from "reactstrap";
import { RouteActors } from './components/ActorView';
import './App.css';

function App() {
  const { loading, user } = useAuth0();

  if (loading && !user) {
    return <p>Loading...</p>
  }
  return (
    <Router history={history}>
      <div id="app" className="d-flex flex-column w-100">
        <NavBar />
        <Container className="flex-grow-1 mt-5">
          <Switch>
            <Route path='/' exact component={Home} />
            <Route path='/movies' component={RouteMovies} />
            <Route path='/actors-details' component={RouteActors} />
          </Switch>
        </Container>
      </div>
    </Router>
  );
}

export default App;
