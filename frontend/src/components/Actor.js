import React from 'react';
import { Col, Card, CardHeader, CardBody, CardFooter, Button } from 'reactstrap';
import { NavLink as RouterNavLink, withRouter } from 'react-router-dom';
import '../App.css';


const ActorItem =  ({actor, exposedToken, token, deleteActor}) => (
        <Col md="4" className="my-3">
            <Card inverse style={{ backgroundColor:'#333', borderColor:'#333'}}>
                <CardHeader style={{fontWeight: "bold"}}>
                    {actor.name}
                </CardHeader>
                <img 
                    width="100%" 
                    // src="https://m.media-amazon.com/images/M/MV5BMjExNzA4MDYxN15BMl5BanBnXkFtZTcwOTI1MDAxOQ@@._V1_UY317_CR7,0,214,317_AL_.jpg"
                    src="https://media0.giphy.com/media/OJ1csu37BS3eg/giphy.webp?cid=ecf05e4703f7b5327442c7cb58adfddedfdfb37ca51a42ff&rid=giphy.webp"
                    alt={actor.name}
                />
                <CardBody>
                    <div>Age: {actor.age}</div>
                    <div>Gender: {actor.gender}</div>
                </CardBody>
                <CardFooter>
                    Movie assigned to: {actor.movie !== null ? (actor.movie) : "None"}
                </CardFooter>
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
                                    tag={RouterNavLink}
                                    to={{pathname:"/actors-details"}}
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