const bcrypt = require('bcrypt');
const saltRounds = 12;

async function hashPasswords() {
    const tester1Password = await bcrypt.hash('Pc4RM0AMKy5aSGfD', saltRounds);
    const tester2Password = await bcrypt.hash('4LWs6xnc1t32BzXA', saltRounds);
    console.log({ tester1Password, tester2Password });
}

hashPasswords();
