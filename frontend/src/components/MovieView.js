import React, { useState, useEffect } from 'react';
import { Container, Row, Button } from 'reactstrap';
import { Navlink as RouteNavlink, Route, Switch } from 'react-router-dom';
// import jwt from 'jwt-decode';
import { useAuth0 } from '../react-auth0-spa';
import { Movie } from './Movie';


const Movies = () => {
    return (
        <>
            <Container>
                <h1>
                    Movies!
                </h1>
            </Container>
        </>
    );
};

export const RouteMovies = () => {
    return (
        <Switch>
            <Route path="/movies" component={Movies} />
        </Switch>
    )
}