// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts@4.8.3/token/ERC1155/ERC1155.sol";
import "@openzeppelin/contracts@4.8.3/access/Ownable.sol";
import "@openzeppelin/contracts@4.8.3/utils/Strings.sol";
import "@openzeppelin/contracts@4.8.3/utils/Counters.sol";


contract MyToken is ERC1155, Ownable {
    constructor() ERC1155("") {
    }

    using Counters for Counters.Counter;
    Counters.Counter private _tokenCounter;
    uint256 public balanceLimit = 16 ether;
    event LowBalance();
    event MintInProgress();
    event MintFinished();

    mapping(uint256 => string) public tokenURIs;
    function setURI(uint256 tokenID, string memory newuri) public onlyOwner {
        tokenURIs[tokenID] = newuri;
    }

    function mint(address account, string memory tokenURI)
        public
        onlyOwner
    {
        emit MintInProgress();
        _mint(account, _tokenCounter.current(), 1,"");
        setURI(_tokenCounter.current(), tokenURI);
        // always increment after mint
        _tokenCounter.increment();
        emit MintFinished();
        // emit event if balance is lowever than defined
        if(msg.sender.balance < balanceLimit){
            emit LowBalance();
        }
    }

    function mintBatch(address to, bytes memory data, string[] memory batchURIs)
        public
        onlyOwner
    {
        // gas efficient to use fixed array size
        uint256[] memory ids = new uint256[](batchURIs.length);
        uint256[] memory amounts = new uint256[](batchURIs.length);

        for(uint256 i=0; i <  batchURIs.length; i++) {
            ids[i] = _tokenCounter.current();
            amounts[i] = 1;

            // set uri
            setURI(ids[i], batchURIs[i]);
            _tokenCounter.increment();
        }
        // mint
        _mintBatch(to, ids, amounts, data);
    }

    // to Put NFT to Opensea
     function uri(uint256 _tokenId) override public view returns (string memory) {
        // require tokenID exists or not
        return tokenURIs[_tokenId];
    }

    function get_random_value() public  view returns (uint256) {
        return 2;
    }

}
