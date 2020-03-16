import React from 'react';
import { Col, Card, Cardbody, CardTitle, CardText, Button } from 'reactstrap';
import { Navlink as RouterNavLink, withRouter } from 'react-router-dom';

const MovieItem = ({movie, exposedToken, token, removeItem}) => (
    <Col md="5" className="my-3">
        <Card>
            <Cardbody>
                <CardTitle>
                    {movie.title}
                </CardTitle>
                <CardText>
                    {movie.release_date}
                </CardText>
                    <div>
                        <Button>
                            Edit
                        </Button>
                        <Button>
                            Delete
                        </Button>
                    </div>
            </Cardbody>
        </Card>
    </Col>
);

export const Movie = withRouter(MovieItem)