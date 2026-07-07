import streamlit as st
from orchestrate_client import generate_blueprint


# ---------------- Page Configuration ---------------- #

st.set_page_config(
    page_title="BlueprintAI",
    page_icon="🚀",
    layout="wide"
)


# ---------------- Custom Styling ---------------- #

st.markdown(
    """
    <style>

    .main-header {
        background: linear-gradient(90deg, #2563EB, #7C3AED);
        padding: 25px;
        border-radius: 15px;
        color: white;
        margin-bottom: 25px;
    }

    .main-header h1 {
        font-size: 42px;
        margin-bottom: 5px;
    }

    .main-header p {
        font-size: 18px;
    }

    .section-title {
        color: #2563EB;
        font-size: 28px;
        font-weight: 700;
    }

    </style>
    """,
    unsafe_allow_html=True
)



# ---------------- Sidebar ---------------- #

with st.sidebar:

    st.title("🚀 BlueprintAI")

    st.write(
        """
        ### AI Startup Blueprint Generator

        """
    )

    st.divider()

    st.subheader("✨ Features")

    st.write(
        """
        ✅ Executive Summary  
        ✅ Market Analysis  
        ✅ Competitor Analysis  
        ✅ Business Model  
        ✅ Revenue Strategy  
        ✅ SWOT Analysis  
        ✅ Growth Roadmap  
        """
    )

    st.divider()

    st.subheader("⚙️ Technology")

    st.write(
        """
        🤖 IBM Watson Orchestrate  
        🎨 Streamlit Interface  
        🧠 AI-Powered Business Analysis
        """
    )

    st.divider()

    st.caption(
        "Powered by IBM Watson Orchestrate"
    )



# ---------------- Header ---------------- #

st.markdown(
    """
    <div class="main-header">

    <h1>🚀 BlueprintAI</h1>

    <p>
    Transform ideas into startup strategies using AI-powered business analysis.
    </p>

    <p>
    Powered by IBM Watson Orchestrate
    </p>

    </div>
    """,
    unsafe_allow_html=True
)


st.subheader(
    "AI-Powered Startup Strategy Generator"
)


st.write(
    """
    Generate complete startup blueprints including market analysis,
    business models, revenue strategies, SWOT analysis and growth roadmap.
    """
)


st.divider()



# ---------------- How It Works ---------------- #

with st.expander("⚙️ How BlueprintAI Works"):

    st.write(
        """
        ### Simple AI Workflow

        💡 Startup Idea  
        ↓  
        📝 User Information Processing  
        ↓  
        🤖 BlueprintAI Agent powered by IBM Watson Orchestrate  
        ↓  
        📊 Business Strategy Generation  
        ↓  
        🚀 Complete Startup Blueprint
        """
    )


st.divider()



# ---------------- Input Form ---------------- #

st.markdown("## 📝 Enter Your Startup Details")


col1, col2 = st.columns(2)


with col1:

    startup_idea = st.text_input(
        "💡 Startup Idea",
        placeholder="AI-powered Hostel Management Platform"
    )


    target_audience = st.text_input(
        "🎯 Target Audience",
        placeholder="Engineering Colleges, Hostel Administrators, Students"
    )


    business_model = st.selectbox(
        "📈 Business Model",
        [
            "SaaS",
            "Subscription",
            "Marketplace",
            "Freemium",
            "B2B",
            "B2C"
        ]
    )


with col2:

    problem_statement = st.text_area(
        "❗ Problem Statement",
        placeholder="Describe the problem your startup solves..."
    )


    budget = st.selectbox(
        "💰 Estimated Budget",
        [
            "Below ₹5 Lakhs",
            "₹5–10 Lakhs",
            "₹10–25 Lakhs",
            "₹25–50 Lakhs",
            "Above ₹50 Lakhs"
        ]
    )


    target_market = st.selectbox(
        "🌍 Target Market",
        [
            "India",
            "Global",
            "College Campuses",
            "Healthcare",
            "Education",
            "Finance"
        ]
    )


st.divider()
# ---------------- Generate Blueprint ---------------- #

if st.button(
    "🚀 Generate Startup Blueprint",
    use_container_width=True
):

    if not startup_idea or not problem_statement:

        st.warning(
            "⚠️ Please provide Startup Idea and Problem Statement."
        )


    else:

        prompt = f"""
You are BlueprintAI, an AI Startup Blueprint Generator.

This request comes from a completed startup submission form.

The user has already provided all the essential information required to generate a startup blueprint.

Do NOT interview the user.
Do NOT ask multiple follow-up questions.

If minor details are missing, make realistic business assumptions and clearly mention them under "Assumptions Made".

Generate the output immediately.

---------------------------
FORM DETAILS
---------------------------

Startup Idea:
{startup_idea}

Target Audience:
{target_audience}

Problem Statement:
{problem_statement}

Business Model:
{business_model}

Estimated Budget:
{budget}

Target Market:
{target_market}

---------------------------


Generate the response in TWO sections:


================================
SECTION 1: BLUEPRINTAI INSIGHTS
================================

Provide short strategic insights.

Include:

📊 Market Opportunity
- Explain the market potential of this startup idea.

💰 Revenue Potential
- Explain how this startup can generate revenue.

⚠️ Key Challenge
- Mention the biggest possible execution challenge.

🎯 Recommended First Step
- Suggest the immediate action the founder should take.

======================================
SECTION 2: COMPLETE STARTUP BLUEPRINT
======================================

Generate a professional Startup Blueprint containing:

1. Executive Summary

2. Problem Statement

3. Proposed Solution

4. Target Audience

5. Market Analysis

6. Competitor Analysis

7. Business Model

8. Revenue Model

9. Funding Opportunities

10. Marketing Strategy

11. SWOT Analysis

12. Development Roadmap

13. Risks & Mitigation

14. Assumptions Made

15. Next Steps


Return the complete response in well-structured Markdown.
"""


        with st.spinner(
            "🚀 BlueprintAI is generating your startup blueprint..."
        ):

            try:

                result = generate_blueprint(prompt)


            except Exception as e:

                st.error(
                    f"❌ Unable to generate blueprint.\n\nError: {e}"
                )

                st.stop()



        st.success(
            "✅ BlueprintAI Generated Your Startup Blueprint Successfully!"
        )


        st.divider()



        # ---------------- Separate Insights and Blueprint ---------------- #

        st.markdown(
            '<p class="section-title">🚀 BlueprintAI Insights</p>',
            unsafe_allow_html=True
        )


        if "SECTION 2: COMPLETE STARTUP BLUEPRINT" in result:

            insights, blueprint = result.split(
                "SECTION 2: COMPLETE STARTUP BLUEPRINT",
                1
            )


            st.markdown(insights)


        else:

            blueprint = result

            st.info(
                "BlueprintAI Insights were not generated separately."
            )



        st.divider()



        # ---------------- Complete Blueprint Output ---------------- #

        st.markdown(
            '<p class="section-title">📄 Complete Startup Blueprint</p>',
            unsafe_allow_html=True
        )


        st.markdown(blueprint)



# ---------------- Footer ---------------- #

st.divider()


st.caption(
    "🚀 BlueprintAI | AI Startup Strategy Assistant | Built using IBM Watson Orchestrate"
)