import React, { useState, useEffect } from 'react';
import { Container, Row, Button } from 'reactstrap';
import { Navlink as RouteNavlink, Route, Switch } from 'react-router-dom';
// import jwt from 'jwt-decode';
import axios from 'axios';
import { useAuth0 } from '../react-auth0-spa';
import { Movie } from './Movie';
import config from '../auth_config.json';

// // const URL = 'https://stephangelcasting.herokuapp.com/movies';
// const URL = 'http://localhost:5000/movies';
// // const DEFAULT_QUERY = '1';

// const Movies = () => {
//    const [result, setResult] = useState({});
//    const [token, setToken] = useState();
//    const { getTokenSilently, user, loading } = useAuth0();

//     return (
//         <div>
//             <h1>
//                 Movies!
//             </ h1>
//             <p>
//                     This is a list of movies to be released soon.
//             </p>
//             <Row>
//                 {
//                     result.movies.map(movie => (
//                         <Movie 
//                             key={movie.id}
//                             movie={movie}
//                             token={token}
//                         />
//                     ))
//                 }
//             </Row>
//         </div>
//     );
// };

// export const RouteMovies = () => {
//     return (
//         <Switch>
//             <Route path="/movies" component={Movies} />
//         </Switch>
//     )
// }

// import React from 'react';
// import axios from 'axios';

export default class Movies extends React.Component {
    state = {
        movies : []
    }

    componentDidMount() {
        axios.get('https://stephangelcasting.herokuapp.com/movies')
            .then(res => {
                const movies = res.data.movies;
                this.setState({ movies });
            })
    }

    render() {
        return (
            <ul>
                { this.state.movies.map(movie => <li>{movie.title} {movie.release_date}</li>)}
            </ul>
        )
    }
}

export const RouteMovies = () => {
    return (
        <Switch>
            <Route path="/movies" component={Movies} />
        </Switch>
    )
}