from fastapi import FastAPI

app = FastAPI()

My_Api = [
    {
        "name": "Ahmed",
        "bio": "Web Developer & AI Enthusiast, specializing in e-commerce solutions, AI agents, and modern UI/UX.",
        "contact": {
            "email": "ahmed@example.com",
            "phone": "+1234567890",
            "website": "https://ahmedxyz.com",
            "github": "https://github.com/ahmedxyz",
            "linkedin": "https://linkedin.com/in/ahmedxyz"
        },
        "skills": [
            "Next.js",
            "React.js",
            "TypeScript",
            "Tailwind CSS",
            "Python",
            "FastAPI",
            "Streamlit",
            "AI Agents",
            "E-commerce Development"
        ],
        "projects": [
            {
                "name": "Bandage Store",
                "description": "An e-commerce store with VIP UI/UX and advanced admin panel.",
                "link": "https://bandage.xyz"
            },
            {
                "name": "Minecraft Store",
                "description": "A store for selling Minecraft-related items with user authentication.",
                "link": "https://minecraftstore.com"
            }
        ],
        "education": [
            {
                "degree": "O Levels",
                "institute": "Gravity Academy",
                "year": "2024"
            },
            {
                "degree": "Self-Taught Developer",
                "institute": "Online Courses & Practical Experience & Governor House I.T",
                "year": "Ongoing"
            }
        ],
        "experience": [
            {
                "role": "Founder & Developer",
                "company": "Cydelon (Web Dev Agency)",
                "year": "2025 - Present",
                "description": "Running a web development agency that builds modern websites and AI-powered applications."
            },
            {
                "role": "Freelance Developer",
                "company": "Upwork & Fiverr",
                "year": "2023 - Present",
                "description": "Providing e-commerce, AI bots, and automation solutions to clients worldwide."
            }
        ],
        "services": [
            {
                "name": "Website Development",
                "description": "Professional and modern websites for businesses and personal brands.",
                "price_range": "$500 - $2000"
            },
            {
                "name": "E-commerce Development",
                "description": "Fully functional e-commerce stores with payment integration.",
                "price_range": "$700 - $3000"
            },
            {
                "name": "AI Chatbots & Agents",
                "description": "Custom AI chatbots and assistants for automation and business solutions.",
                "price_range": "$1000 - $5000"
            }
        ],
        "pricing": {
            "basic_website": "$500",
            "advanced_website": "$1200",
            "ecommerce_store": "$2000",
            "custom_ai_agent": "$3000"
        }
    }
]

@app.get("/ahmed-api")
def Ahmed_Data():
    return {"data": My_Api}