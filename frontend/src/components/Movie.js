import React from 'react';
import { Col, Card, CardBody, CardTitle, CardText, Button } from 'reactstrap';
import { NavLink as RouterNavLink, withRouter } from 'react-router-dom';
import '../App.css';

const MovieItem = ({movie, exposedToken, token, deleteMovie}) => (
    <Col md="5" className="my-3">
        <Card inverse style={{ backgroundColor:'#333', borderColor:'#333'}}>
            <CardBody>
                <CardTitle>
                    {movie.title}
                </CardTitle>
                <CardText>
                    Release Date: {movie.release_date}
                </CardText>
                <div className="clearfix p-2">
                    {exposedToken &&
                        exposedToken.permissions.indexOf("patch:movies") !== -1 ? (
                            <Button
                                outline color="primary"
                                className="float-left"
                                tag={RouterNavLink}
                                to={{
                                    pathname: '/movies/AddNewMovie',
                                    state: { movie, editing: true, token }
                                }}
                            >
                                Edit
                            </Button>
                        ) : null}
                    {exposedToken && 
                        exposedToken.permissions.indexOf("delete:movies") !== -1 ? (
                            <Button
                                outline color="danger"
                                tag={RouterNavLink}
                                to="/movies"
                                className="float-right"
                                onClick={() => deleteMovie(movie.id)}
                            >
                                Delete
                            </Button>
                    ) : null}
                </div>
            </CardBody>
        </Card>
    </Col>
);

export const Movie = withRouter(MovieItem);