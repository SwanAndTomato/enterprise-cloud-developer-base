const AWS = require('aws-sdk');
const bcrypt = require('bcrypt');
const jwt = require('jsonwebtoken');

const dynamo = new AWS.DynamoDB.DocumentClient();
const SECRET = '0HXc4w5NEzA61HkV';
const TOKEN_EXPIRATION = '1h';

exports.handler = async (event) => {
    try {
        const { username, password } = JSON.parse(event.body);

        if (!username || !password) {
            return { statusCode: 403, body: JSON.stringify({ message: 'Invalid credentials' }) };
        }

        // Query the users table
        const params = {
            TableName: 'users',
            Key: { username },
        };

        const user = await dynamo.get(params).promise();

        if (!user.Item || !(await bcrypt.compare(password, user.Item.password))) {
            return { statusCode: 403, body: JSON.stringify({ message: 'Invalid credentials' }) };
        }

        // Generate JWT
        const token = jwt.sign({ username }, SECRET, { expiresIn: TOKEN_EXPIRATION });
        return {
            statusCode: 200,
            body: JSON.stringify({
                token,
                expiresAt: new Date(Date.now() + 60 * 60 * 1000).toISOString(),
            }),
        };
    } catch (error) {
        console.error(error);
        return { statusCode: 500, body: JSON.stringify({ message: 'Internal server error' }) };
    }
};
