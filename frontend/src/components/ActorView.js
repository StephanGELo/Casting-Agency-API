import React, { useState, useEffect } from "react";
import { Container, Row, Button } from 'reactstrap';
import { Route, Switch } from 'react-router-dom';

const Actors = () => {
    return (
        <Container>
            <h1>Recent Actors</h1>
        </Container>
    );
};

export const RouteActors = () => (
    <Switch>
        <Route path="/actors" component={Actors} />
    </Switch>
);