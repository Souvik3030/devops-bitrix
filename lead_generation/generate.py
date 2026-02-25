from faker import Faker

fake = Faker()

real_estate_lexicon = [
    # Land & Physical Attributes
    "Acreage", "Plot", "Topography", "Zoning", "Easement", "Encroachment", 
    "Survey", "Setback", "FSI", "Landlocked", "Greenfield", "Brownfield", 
    "Frontage", "Demarcation", "Percolation", "Soil Test", "Parcel", "Lot", 
    "Grading", "Utility Hookup", "Right of Way", "Buffer Zone", "Metes and Bounds",
    
    # Legal & Documentation
    "Deed", "Title", "Abstract", "Clear Title", "POA", "Sale Deed", 
    "Allotment", "Encumbrance", "Conveyance", "Mutation", "RERA", "Indemnity", 
    "MOU", "Lien", "Covenant", "Escrow", "Probate", "Notary", "Registry", 
    "Bylaws", "Freehold", "Leasehold", "Adverse Possession", "Quiet Title",
    
    # Financial & Investment
    "Appraisal", "ROI", "Cap Rate", "Valuation", "Earnest Money", "Escalation", 
    "Equity", "Leverage", "Amortization", "Mortgage", "Closing Costs", "LTV", 
    "Appreciation", "Depreciation", "Capital Gains", "Stamp Duty", "Foreclosure", 
    "Pre-approval", "Refinance", "Underwriting", "Hard Money", "Balloon Payment",
    
    # Business & Market Terms
    "Brokerage", "Commission", "MLS", "Escalation Clause", "Comps", "Listing", 
    "Off-market", "Wholesaling", "Flipping", "Arbitrage", "Due Diligence", 
    "Feasibility", "Turnkey", "As-is", "Letter of Intent", "Contingency", 
    "Force Majeure", "Inventory", "Absorption Rate", "Buyer's Market", "Seller's Market",
    
    # Inquiry & Development
    "Site Visit", "Conversion", "Development Rights", "Joint Venture", 
    "Master Plan", "Phasing", "Infrastructure", "Amenities", "Possession", 
    "Handover", "Maintenance", "Occupancy Certificate", "Completion Certificate", 
    "Drafting", "Blueprints", "Floor Plan", "Spec Home", "Built-to-suit"
]

def generate_name() -> str:
    return fake.name()

def generate_title() -> str:
    return fake.sentence(ext_word_list=real_estate_lexicon)

def generate_phone() -> str:
    number = fake.phone_number()
    if "x" in number:
        pos = number.find("x")
        number = number[0:pos]
    return number

if __name__ == "__main__":
    for _ in range(11):
        print(generate_title(), generate_name(), generate_phone())