import React from 'react';
import { Col, Card, CardHeader, CardBody, CardFooter} from 'reactstrap';
import { withRouter } from 'react-router-dom';

const ActorItem = (props) => {
    return (
        <Col md="4" className="my-3">
            <Card>
                <CardHeader style={{fontWeight: "bold"}}>
                    {props.actor.name}
                </CardHeader>
                <img 
                    width="100%" 
                    // src="https://m.media-amazon.com/images/M/MV5BMjExNzA4MDYxN15BMl5BanBnXkFtZTcwOTI1MDAxOQ@@._V1_UY317_CR7,0,214,317_AL_.jpg"
                    src="https://media0.giphy.com/media/OJ1csu37BS3eg/giphy.webp?cid=ecf05e4703f7b5327442c7cb58adfddedfdfb37ca51a42ff&rid=giphy.webp"
                    alt="Vin Diesel"
                />
                <CardBody>
                    <div>Age: {props.actor.age}</div>
                    <div>Gender: {props.actor.gender}</div>
                </CardBody>
                <CardFooter>
                    Movie assigned to: {props.actor.movie}
                </CardFooter>
            </Card>
        </Col>
    );
};

export const Actor = withRouter(ActorItem);