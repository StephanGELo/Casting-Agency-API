import React from 'react';
import { Col, Card, CardHeader, CardBody, CardFooter, CardImg, Button } from 'reactstrap';
import { NavLink as RouterNavLink, withRouter } from 'react-router-dom';
import '../App.css';


const ActorItem =  ({actor, exposedToken, token, deleteActor}) => (
        <Col md="3" className="my-2">
            <Card inverse style={{ backgroundColor:'#333', borderColor:'#333', height:'500px'}}>
                <CardHeader style={{fontWeight: "bold", backgroundColor:'orange', color:"black"}}>
                    {actor.name}
                </CardHeader>
                <CardImg 
                    width="100%" 
                    height="50%"
                    src={actor.image_link}
                    alt={actor.name}
                />
                <CardBody style={{fontFamily: "Open Sans Condensed", color:"silver"}}>
                    <div>Age: {actor.age}</div>
                    <div>Gender: {actor.gender}</div>
                </CardBody>
                <CardBody>
                    Movie assigned to: {actor.movie !== null ? (actor.movie) : "None"}
                </CardBody>
                <CardFooter >
                    <div className="clearfix p-2">
                        {exposedToken && 
                            exposedToken.permissions.indexOf("patch:actors") !== -1 ? (
                                <Button 
                                    outline color="primary"
                                    className="float-left"
                                    tag={RouterNavLink}
                                    to ={{
                                        pathname: "/actors-details/addNewActor",
                                        state: { editing: true, actor, token}
                                    }}
                                >
                                    Edit
                                </Button>
                            ) : null
                        }
                        {exposedToken &&
                            exposedToken.permissions.indexOf("delete:actors") !== -1 ? (
                                <Button
                                    outline color="danger"
                                    className="float-right"
                                    onClick={() => deleteActor(actor.id)}
                                >
                                    Delete
                                </Button>
                            ) : null
                        }
                    </div>
                </CardFooter>
            </Card>
        </Col>
);

export const Actor = withRouter(ActorItem);