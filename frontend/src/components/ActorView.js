import React, { useState, useEffect } from "react";
import { Container, Row, Button } from 'reactstrap';
import { Route, Switch } from 'react-router-dom';
import { Actor } from "./Actor";

const Actors = () => {
    return (
        <>
            <Container>
                <h1>Recent Actors</h1>
                <Button color='primary' style="text-right">Add a New Actor</Button>
                <Row>
                    <Actor />
                </Row>
            </Container>
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