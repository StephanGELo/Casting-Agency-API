import React, { useState, useEffect } from "react";
import { Container, Row, Button } from 'reactstrap';
import { Route, Switch } from 'react-router-dom';

const Actors = () => {
    return (
        <>
            <div>
                <h1>Recent Actors</h1>
            </div>
        </>
    );
};

export const RouteActors = () => {
    return (
        <Switch>
            <Route path="/actors" component={Actors} />
        </Switch>
    );
};