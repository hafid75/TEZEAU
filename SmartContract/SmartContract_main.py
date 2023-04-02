import smartpy as sp
FA2 = sp.io.import_template("FA2.py")

class NFT(FA2.FA2):
   pass
    
################
    # Vote #
################
class Vote(sp.Contract):
    def __init__(self,address,add_nft):
        self.init(
            admin = address,
            address_nft = add_nft,
            users = sp.big_map(
                tkey=sp.TAddress,
                tvalue=sp.TRecord(
                    option_vote = sp.TString, token_id = sp.TIntOrNat
                )
            ),
            votes = sp.map(tkey=sp.TString, tvalue=sp.TInt)
        )

    #fonction qui créé les options de vote
    @sp.entry_point
    def definitionVote(self, params):
        sp.set_type(params, sp.TRecord(option1=sp.TString,option2=sp.TString,option3=sp.TString))
        option1 = params.option1
        option2 = params.option2
        option3 = params.option3
        
        newOptions = {option1 : 0, option2 : 0 ,option3: 0}
        self.data.votes = newOptions

    #fonction qui ajoute le possesseur du nft dans la map
    @sp.entry_point
    def ajoutVotant(self, params):
        sp.set_type(params, sp.TRecord(option=sp.TString, token_id=sp.TIntOrNat,questionnaireIsDone=sp.TBool))
        option = params.option
        token_id = params.token_id
        questionnaireIsDone = params.questionnaireIsDone

        sp.verify(questionnaireIsDone==True, "N'a pas répondu au questionnaire")
        
        self.data.users[sp.sender] = sp.record(option_vote=option, token_id=token_id)
        #self.data.users[sp.sender].option_vote = option
        #self.data.users[sp.sender].token_id = token_id
        
        
    #fonction qui fais voter la personne
    @sp.entry_point
    def vote(self):
        sp.verify(self.data.users.contains(sp.sender), "non autorisé à voter car il n'a pas répondu au questionnaire")
        
        option = self.data.users[sp.sender].option_vote
        sp.trace(option)
        self.data.votes[option] += 1
        

################
# Quizz #
################
class Quizz(sp.Contract):
    def __init__(self,address,time):
        self.init(
            admin = "tz1admin",
            user=address,
            answer1 = "",
            answer2 = "",
            answer3 = "",
            passed = False,
            time = time
        )
    
    #fonction qui créé les réponses
    @sp.entry_point
    def setAnswers(self,params):
        sp.set_type(params, sp.TRecord(answer1=sp.TString,answer2=sp.TString,answer3=sp.TString))
        self.data.answer1 = params.answer1
        self.data.answer2 = params.answer2
        self.data.answer3 = params.answer3

    #view qui retourne qi l'utilisateur a repondu au questionnaire ou non
    @sp.onchain_view()
    def questionnaireIsOk(self):
        sp.result(self.data.passed)

    #fonction qui vérifie les réponses
    @sp.entry_point
    def takequizz(self,params):
        sp.set_type(params, sp.TRecord(answer1=sp.TString,answer2=sp.TString,answer3=sp.TString))

        sp.verify(self.data.passed==False, "Quizz déjà réussi")
        
        #S'il a echoué il y'a moins de 2 heures au quizz il ne pourra pas recommencer le quizz
        sp.verify(sp.timestamp_from_utc_now() >= self.data.time.add_seconds(2*60*60), "Vous devez attendre 2 heures avant de pouvoir répondre à nouveau.")
   
        score = 0
        sp.if params.answer1 == self.data.answer1:
            score += 1
        sp.if params.answer2 == self.data.answer2:
            score += 1
        sp.if params.answer3 == self.data.answer3:
            score += 1
         
        #Quizz echoué s'il a pas 3 sur 3
        sp.if score < 3:
            self.data.time = sp.now
            sp.failwith("Vous avez échoué le quizz. Veuillez réessayer dans 2 heures.")
        sp.else:
            self.data.passed = True


@sp.add_test(name = "main")
def test():
    time = sp.timestamp(0)
    scenario = sp.test_scenario()

    admin = sp.test_account("tz1admin")
    Alice = sp.test_account("Alice")
    Bob = sp.test_account("Bob")


    Q_A = Quizz(Alice.address,time)
    scenario += Q_A

    Q_B = Quizz(Bob.address,time)
    scenario += Q_B

    # création des réponses
    scenario += Q_A.setAnswers(answer1="R1",answer2="R2",answer3="R3").run()

    # reponse aux question
    scenario += Q_A.takequizz(answer1="R1",answer2="R2",answer3="R3").run(valid=True)

    # reponse sachant qu'il a déjà répondu
    scenario += Q_A.takequizz(answer1="R1",answer2="R2",answer3="R3").run(valid=False)


    #Mint du nft pour alice
    nft1 = NFT(FA2.FA2_config(non_fungible=True), admin=admin.address, metadata= sp.big_map({"": sp.utils.bytes_of_string("tezos-storage:content"),"content": sp.utils.bytes_of_string("""{"name": "TezEau responsable", "description": "Avec ce NFT vous pouerrez votez"}""")}))
    scenario += nft1
    nft1.mint(token_id=0, address=Alice.address, amount=1, metadata = sp.map({"": sp.utils.bytes_of_string("ipfs://bafkreih36m3d4yfbpyteluvntuph5xybwtgxdvyksbgyg66es44drk4hqy")})).run(sender=admin)
    
    #Mint du nft pour Bob
    nft2 = NFT(FA2.FA2_config(non_fungible=True), admin=admin.address, metadata= sp.big_map({"": sp.utils.bytes_of_string("tezos-storage:content"),"content": sp.utils.bytes_of_string("""{"name": "TezEau responsable", "description": "Avec ce NFT vous pouerrez votez"}""")}))
    scenario += nft2
    nft2.mint(token_id=0, address=Alice.address, amount=1, metadata = sp.map({"": sp.utils.bytes_of_string("ipfs://bafkreih36m3d4yfbpyteluvntuph5xybwtgxdvyksbgyg66es44drk4hqy")})).run(sender=admin)

    V = Vote(Alice.address,nft1.address)
    scenario += V

    V = Vote(Bob.address,nft2.address)
    scenario += V

    #definition des votes
    scenario += V.definitionVote(option1="Traitement pour une utilisation non potable", 
                          option2="Traitement pour une utilisation potable", 
                          option3="Traitement pour une utilisation industrielle")

    #Vérification du vote d'Alice
    scenario.show(Q_A.questionnaireIsOk())
    verify = Q_A.questionnaireIsOk()
    # Ajout du votant Alice
    scenario += V.ajoutVotant(option="Traitement pour une utilisation potable", token_id=0,questionnaireIsDone=verify).run(valid=True,
        sender = Alice
    )
    
    
    #Vérification du vote de Bob
    scenario.show(Q_B.questionnaireIsOk())
    verify = Q_B.questionnaireIsOk()
    # Ajout du votant Bob (ne pourra pas car n'a pas répondu au quizz)
    scenario += V.ajoutVotant(option="Traitement pour une utilisation potable", token_id=0,questionnaireIsDone=verify).run(valid=False,
        sender = Bob
    )
    
    # Vote par l'utilisateur Alice (possédant le nft et ayant répondu au sondage)
    scenario += V.vote().run(valid=True,
        sender = Alice
    )

        # Vote par l'utilisteur Bob (ne possédant pas le nft et ayant pas répondu au sondage)
    scenario += V.vote().run(valid=False,
        sender = Bob
    )

    # Vote par l'utilistaue (ne possédant pas le nft et ayant répondu au sondage)
    scenario += V.vote().run(valid=False,
        sender = admin
    )

    
