import React, { useState, useEffect } from "react";
import { Container, Row, Button } from "reactstrap";
import { NavLink as RouterNavLink, Route, Switch } from "react-router-dom";
import jwt from "jwt-decode";
import { useDataFetching } from "../hooks/useDataFetch";
import { useAuth0 } from "../react-auth0-spa";
import { Movie } from "./Movie";
import { API_URL } from "../utils/auth_config";
import { Loader } from "./Loader";

const Movies = () => {
    const [response, setResponse] = useState({});
    const [pageNum, setPageNum] = useState(1);
    const [token, setToken] = useState();
    const { getTokenSilently, user, loading } = useAuth0();

    const url = `${API_URL}/movies?page=${pageNum}`;
    console.log("url is: ", url)
    const result = useDataFetching(url, {}, token) || {};

    useEffect(() => {
        setResponse(result)
    }, [result])

    if (user && !loading) getTokenSilently().then(res => setToken(res));

    let decodedToken;
    if (token) decodedToken = jwt(token);

    const selectPage = num => setPageNum(num);
    const create_pagination = () => {
        let pageNumbers = [];
        let maxPage = Math.ceil(result.total_movies / 10);

        for (let i = 1; i <= maxPage; i++) {
            pageNumbers = [
                ...pageNumbers,
                <span
                    key={i}
                    className={`page-num ${i === pageNum ? "active" : ""}`}
                    onClick={() => {
                        selectPage(i);
                    }}
                >
                    {i}
                </span>
            ];
        }
        return pageNumbers;
    };

    const deleteMovie = async id => {
        const result = await fetch(`${API_URL}/movies/${id}`, {
            method: "DELETE",
            headers: {
                Authorization: "Bearer " + token,
                "Content-Type": "application/json"
            }
        });
        const getResult = await result.json()
        setResponse(getResult)
    };

    return (
        <>
            <Container>
                <h1>Recent Movies</h1>
                {decodedToken &&
                    decodedToken.permissions.indexOf("post:movies") !== -1 ? (
                        <Button color="primary" to={{
                            pathname: "/movies/add-movie",
                            state: { editing: false, movieData: null, token: token }
                        }} tag={RouterNavLink}>
                            Add a movie
                        </Button>
                    ) : null}
                <Row>
                    {response.movies ? (
                        response.movies.map(movie => (
                            <Movie
                                key={movie.id}
                                movie={movie}
                                exposedToken={decodedToken}
                                token={token}
                                deleteMovie={deleteMovie}
                            />
                        ))
                    ) : (
                            <Loader />
                        )}
                </Row>
                <Row className="justify-content-center">{create_pagination()}</Row>
            </Container>
        </>
    );
};

export const RouteMovies = () => {
    return (
        <Switch>
            {/* <Route path="/movies/add-movie" component={AddMovie} /> */}
            <Route path="/movies" component={Movies} />
        </Switch>
    )
}