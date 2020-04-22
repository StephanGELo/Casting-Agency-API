import React from 'react';
import { Col, Card, CardBody, CardHeader, CardFooter, CardImg, Button } from 'reactstrap';
import { NavLink as RouterNavLink, withRouter } from 'react-router-dom';
import '../App.css';

const MovieItem = ({movie, exposedToken, token, deleteMovie}) => (
    <Col md="3" className="my-2" >
        <Card inverse style={{ backgroundColor:'#333', borderColor:'#333', height:'500px'}}>
             <CardHeader style={{fontWeight: "bold", backgroundColor:'orange', color:"black"}}>
                {movie.title}
            </CardHeader>
            <CardImg 
                width="100%"
                height="50%"
                src={movie.image_link}
                alt={movie.name}
            />
            <CardBody style={{fontFamily:"Open Sans Condensed", color:"silver"}}>
                <div>Release Date: {movie.release_date}</div>
                <div>Cast: {" "}
                    {
                        movie.actors.length !== 0 ?
                            movie.actors.join(", ")
                        : " TBA"
                    }
                </div>
            </CardBody>
            <CardFooter height="10%">
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
                                className="float-right"
                                onClick={() => deleteMovie(movie.id)}
                            >
                                Delete
                            </Button>
                    ) : null}
                </div>
            </CardFooter>
        </Card>
    </Col>

);

export const Movie = withRouter(MovieItem);