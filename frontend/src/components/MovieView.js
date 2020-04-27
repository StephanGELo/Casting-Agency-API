import React, { useState, useEffect } from "react";
import { Container,CardDeck, Row, Button } from "reactstrap";
import { NavLink as RouterNavLink, Route, Switch } from "react-router-dom";
import * as JWT from 'jwt-decode';
import { useAuth0 } from "../react-auth0-spa";
import { API_URL } from "../utils/auth_config";
import { useDataFetching } from "../hooks/useDataFetch";
import { Loader } from "./Loader";
import { Movie } from "./Movie";
import { AddMovieForm } from "./Forms/AddMovieForm";

const Movies = () => {
    const [response, setResponse] = useState({});
    const [pageNum, setPageNum] = useState(1);
    const [token, setToken] = useState();
    const { getTokenSilently, user, loading } = useAuth0();

    const url = `${API_URL}/movies?page=${pageNum}`;

    const result = useDataFetching(url, {}, token) || {};

    useEffect(() => {
        setResponse(result)
    }, [result])

    if (user && !loading) getTokenSilently().then(res => setToken(res));

    let decodedToken;

    try {
        if (token){
            decodedToken = JWT(token)
        }
    } catch(error) {
        console.log(error)
    }
    


    const selectPage = num => setPageNum(num);
    const create_pagination = () => {
        let pageNumbers = [];
        
       let maxPage = Math.ceil(result.total_movies / 10);
            // console.log("maxpage is ", result.movies.length)
     

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
                    {i + " "}
                </span>
            ];
        }
        return pageNumbers;
    };

    const deleteMovie = async id => {
        const result = await fetch(`${API_URL}/movies/${id}`, {
            method: "DELETE",
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
                <h1>Recent Movies</h1>
                {decodedToken && decodedToken.permissions.indexOf("post:movies") !== -1 ? (
                    <div className="text-right">
                        <Button outline color="primary" to={{
                            pathname: "/movies",
                            state: { editing: false, movie: null, token: token }
                        }} tag={RouterNavLink}>
                            Add a movie
                        </Button>
                    </div>
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
            <Route path="/movies/addNewMovie" component={AddMovieForm} />
            <Route path="/movies" component={Movies} />
        </Switch>
    )
}