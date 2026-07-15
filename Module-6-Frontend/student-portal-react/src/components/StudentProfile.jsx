import{ useState } from 'react';

function StudentProfile() {
  // Task 74: Own local state (name, email, semester)
        const [profile, setProfile] = useState({
                name: '',
                email: '',
                semester: ''
        });

  // Generic onChange handler bound to inputs
        const handleChange = (e) => {
                const { name, value } = e.target;
                setProfile((prevProfile) => ({
                        ...prevProfile,
                        [name]: value // Dynamically updates name, email, or semester
                }));
        };

        const handleSubmit = (e) => {
                e.preventDefault();
                alert(`Profile Saved!\nName: ${profile.name}\nEmail: ${profile.email}\nSemester: ${profile.semester}`);
                console.log('Saved Profile:', profile);
        };

        return (
                <div style={profileContainer}>
                        <h3>Student Profile</h3>
                        <form onSubmit={handleSubmit} style={formStyle}>
                        <div>
                                <label style={labelStyle}>Name:</label>
                                <input
                                type="text"
                                name="name"
                                value={profile.name}
                                onChange={handleChange}
                                placeholder="Enter your name"
                                style={inputStyle}
                                required
                                />
                        </div>

                        <div>
                                <label style={labelStyle}>Email:</label>
                                <input
                                type="email"
                                name="email"
                                value={profile.email}
                                onChange={handleChange}
                                placeholder="Enter your email"
                                style={inputStyle}
                                required
                                />
                        </div>

                        <div>
                                <label style={labelStyle}>Semester:</label>
                                <input
                                type="text"
                                name="semester"
                                value={profile.semester}
                                onChange={handleChange}
                                placeholder="e.g., Fall 2026"
                                style={inputStyle}
                                required
                                />
                        </div>

                        <button type="submit" style={buttonStyle}>Save Profile</button>
                        </form>
                </div>
        );
}

// Simple styling
const profileContainer = {
        minWidth:'30rem',
        border: '1px solid #ccc',
        padding: '20px',
        marginTop: '30px',
        maxWidth: '400px',
        backgroundColor: '#c4f2fc'
};

const formStyle = {
        display: 'flex',
        flexDirection: 'column',
        gap: '15px'
};

const labelStyle = {
        fontWeight: 'bold',
        display: 'block',
        marginBottom: '5px'
};

const inputStyle = {
        width: '100%',
        boxSizing: 'border-box',
        border: '1px solid grey'
};

const buttonStyle = {
        padding: '10px',
        backgroundColor: '#4297eb',
        color: 'white',
        border:'none',
        fontWeight: 'bold'
};

export default StudentProfile;