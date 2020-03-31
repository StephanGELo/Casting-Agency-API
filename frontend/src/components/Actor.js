import React from 'react';
import { Card, CardHeader, CardBody, CardFooter} from 'reactstrap';
import { withRouter } from 'react-router-dom';

const ActorItem = () => {
    return (
        <>
            <Card>
                <CardHeader>
                    Actor's Name
                </CardHeader>
                <img 
                    width="100%" 
                    // src="https://m.media-amazon.com/images/M/MV5BMjExNzA4MDYxN15BMl5BanBnXkFtZTcwOTI1MDAxOQ@@._V1_UY317_CR7,0,214,317_AL_.jpg"
                    src="https://media0.giphy.com/media/OJ1csu37BS3eg/giphy.webp?cid=ecf05e4703f7b5327442c7cb58adfddedfdfb37ca51a42ff&rid=giphy.webp"
                    alt="Vin Diesel"
                />
                <CardBody>
                    Actor's Age
                </CardBody>
                <CardBody>
                    Actor's Gender
                </CardBody>
                <CardFooter>
                    Movie assigned to:
                </CardFooter>
            </Card>
        </>
    );
};

export const Actor = withRouter(ActorItem);