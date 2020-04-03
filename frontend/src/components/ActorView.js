import React, { useState, useEffect } from "react";
import { Container, Row, Button } from 'reactstrap';
import { NavLink as RouterNavLink, Route, Switch } from 'react-router-dom';
import { Actor } from "./Actor";
import { useAuth0 } from "../react-auth0-spa";
import { useDataFetching } from "../hooks/useDataFetch";
import { Loader } from "./Loader";
import { API_URL } from "../utils/auth_config";
import * as JWT from 'jwt-decode';
import { AddActorForm } from "./Forms/AddActorForm";


const Actors = () => {
    const [response, setResponse] = useState({});
    const [token, setToken] = useState();
    const { getTokenSilently, user, loading } = useAuth0();

    const url = `${API_URL}/actors-details`;

    const result = useDataFetching(url, {}, token) || {};

    useEffect(() => {
        setResponse(result)
    }, [result])

    if (user && !loading) getTokenSilently().then(res => setToken(res));

    let decodedToken;

    try {
        if (token) {
            decodedToken = JWT(token)
        }
    } catch(error) {
        console.log(error)
    }

    const deleteActor = async id => {
        const result = await fetch(`${API_URL}/actors/${id}`, {
            method: 'DELETE',
            headers: {
                "Authorization": "Bearer " + token,
                "Content-Type": "application/json"
            }
        });
        const getResult = await result.json()
        setResponse(getResult)
    };
    
    return (
        <>
            <Container>
                <h1>Recent Actors</h1>
                {decodedToken && decodedToken.permissions.indexOf("post:actors") !== -1 ? (
                    <div className="text-right">
                        <Button color="primary" to={{
                            pathname:"/actors-details/AddNewActor",
                            state: { editing: false, actor:null, token: token }
                        }} tag={RouterNavLink}>
                        Add a New Actor
                        </Button>
                    </div>
                    ): null}
                <Row>
                    {response.actors ? (
                        response.actors.map(actor => (
                            <Actor 
                                key={actor.id}
                                actor={actor}
                                exposedToken={decodedToken}
                                token={token}
                                deleteActor={deleteActor}
                            />
                        ))
                    ) : (
                            <Loader />
                        )
                    }
                </Row>
            </Container>
        </>
    );
};

export const RouteActors = () => {
    return (
        <Switch>
            <Route path="/actors-details/AddNewActor" component={AddActorForm} />
            <Route path="/actors-details" component={Actors} />
        </Switch>
    );
};