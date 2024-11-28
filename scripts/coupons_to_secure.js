const jwt = require('jsonwebtoken');
const SECRET = '0HXc4w5NEzA61HkV';

exports.handler = async (event) => {
    try {
        const token = event.headers.Authorization;

        if (!token) {
            return { statusCode: 403, body: JSON.stringify({ message: 'Token required' }) };
        }

        try {
            jwt.verify(token, SECRET);
            return { statusCode: 200, body: JSON.stringify({ message: 'Token is valid' }) };
        } catch (err) {
            return { statusCode: 403, body: JSON.stringify({ message: 'Invalid token' }) };
        }
    } catch (error) {
        console.error(error);
        return { statusCode: 500, body: JSON.stringify({ message: 'Internal server error' }) };
    }
};
